#!/usr/bin/env node
// response.js - Enhanced Minecraft server scanner with BungeeHack detection

const mc = require('minecraft-protocol');

// === Constants and Configuration ===
const SEP = '/#FuckTool#/';
const CONNECTION_TIMEOUT = 5000; // 5 seconds
const RECONNECT_DELAY = 1000;    // 1 second delay for BungeeHack retry
const LOGIN_DELAY = 3000;        // 3 seconds delay after login

// === CLI Argument Validation ===
if (process.argv.length < 6) {
    console.error('Usage: node response.js <host> <port> <version> <username>');
    process.exit(1);
}

const [,, host, portStr, version, username] = process.argv;
const port = parseInt(portStr, 10);

// === State Management ===
let useBungeeHack = false;
let connectionEstablished = false;

// === Utility Functions ===
function cleanText(text) {
    return text.replace(/\s+/g, ' ').trim();
}

function extractVersionFromError(message) {
    const versionMatch = message.match(/\d+\.\d+\.\d+/);
    return versionMatch ? versionMatch[0] : version;
}

// === JSON Processing ===
function getTextFromJSON(jsonString) {
    let parsed;
    try {
        parsed = typeof jsonString === 'string' ? JSON.parse(jsonString) : jsonString;
    } catch {
        return jsonString;
    }

    let result = '';
    
    function traverse(node) {
        if (!node) return;
        
        if (node.text) result += node.text;
        if (node.translate) result += node.translate;
        
        if (node.extra) {
            if (Array.isArray(node.extra)) {
                node.extra.forEach(traverse);
            } else {
                traverse(node.extra);
            }
        }
        
        if (node.with) {
            if (Array.isArray(node.with)) {
                node.with.forEach(traverse);
            } else {
                traverse(node.with);
            }
        }
    }

    traverse(parsed);
    return cleanText(result) || jsonString;
}

// === Output Handling ===
function outputAndExit(message, brand = '', channels = '') {
    console.log([cleanText(message), brand, channels].join(SEP));
    process.exit(0);
}

// === Connection Management ===
function createClient(fakeHost = null) {
    const options = {
        host,
        port,
        username,
        version,
        fakeHost,
        hideErrors: true,
        connectTimeout: CONNECTION_TIMEOUT
    };

    const client = mc.createClient(options);
    let brand = '';
    let pluginChannels = '';

    // Event Handlers
    client.on('custom_payload', (packet) => {
        try {
            const data = packet.data.toString('utf8');
            if (packet.channel === 'minecraft:brand') {
                brand += data;
            } else if (packet.channel === 'minecraft:register') {
                pluginChannels += data;
            }
        } catch (e) {
            // Ignore payload parsing errors
        }
    });

    client.on('login', () => {
        connectionEstablished = true;
        setTimeout(() => {
            const status = useBungeeHack ? '&dConnected with BungeeHack' : '&aConnected';
            outputAndExit(status, brand, pluginChannels);
        }, LOGIN_DELAY);
    });

    client.on('disconnect', (packet) => {
        const reason = getTextFromJSON(packet.reason);
        
        if (!useBungeeHack && reason.includes('IP forwarding')) {
            useBungeeHack = true;
            console.log('Reconnecting with BungeeHack...');
            const hackHost = `${host}\u0000127.0.0.1\u0000${client.uuid || 'bdf844e7-54f3-39c9-b577-b275f5753e80'}`;
            setTimeout(() => createClient(hackHost), RECONNECT_DELAY);
            return;
        }
        
        outputAndExit(reason, '', '');
    });

    client.on('error', (err) => {
        const message = err.message;
        
        if (message.includes('you are using version')) {
            const v = extractVersionFromError(message);
            outputAndExit(`&7Please use version ${v} to enter the server.`, '', '');
        } else if (message.includes('is not supported')) {
            const v = extractVersionFromError(message);
            outputAndExit(`&cIncompatible version: ${v}`, '', '');
        } else if (!connectionEstablished) {
            outputAndExit(`&cConnection error: ${cleanText(message)}`, '', '');
        }
    });

    return client;
}

// === Server Ping ===
function pingServer(callback) {
    mc.ping({ host, port, timeout: CONNECTION_TIMEOUT }, (err, result) => {
        if (err) return callback(err);
        
        const motd = typeof result.description === 'string' 
            ? result.description 
            : result.description.text || JSON.stringify(result.description);
            
        callback(null, {
            latency: result.latency,
            version: result.version.protocol,
            motd: cleanText(motd)
        });
    });
}

// === Main Execution ===
// Global timeout
setTimeout(() => {
    if (!connectionEstablished) {
        outputAndExit(useBungeeHack ? '&cTimeout (BungeeHack attempt)' : '&cTimeout', '', '');
    }
}, CONNECTION_TIMEOUT + 1000);

// Initial ping and connection
pingServer((err, info) => {
    if (err) {
        outputAndExit(`&cPing failed: ${cleanText(err.message)}`);
    } else {
        console.log(`Ping: ${info.latency}ms, Protocol: ${info.version}, MOTD: ${info.motd}`);
    }
    createClient();
});