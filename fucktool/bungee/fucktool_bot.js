/*
This bot can connect to a Minecraft server and retrieve the server brand and registered channels.
It supports two modes:
1. none Mode (none):
- Connects with a username and attempts to retrieve the brand and channels.
2. FakeHost Mode (fakehost):
- Connects with a fake host to connect to a BungeeCord backend server.
*/

class MinecraftBot {
    constructor({ ip, port, mode = 'none', username = 'FTool' }) {
        this.ip = ip;
        this.port = port;
        this.version = false;
        this.username = username;
        this.brand = '';
        this.channels = [];
        this.ready = false;
        this.gotBrand = false;
        this.gotChannels = false;
        this.mode = mode; // 'none' or 'fakehost'
        this.hasRetried = false;

        this._initClient();
    }

    _initClient() {
        const mp = require('minecraft-protocol');

        const options = {
            host: this.ip,
            port: this.port,
            version: this.version,
            username: this.username,
        };

        if (this.mode === 'fakehost') {
            const fakeHost = `${this.ip}\x00127.0.0.1\x00e9e21092-7627-4ff0-9f11-b9898d0beb42`;
            options.username = 'FTool-Scanner';
            options.fakeHost = fakeHost;
        }

        this.bot = mp.createClient(options);

        this.bot.on('connect', () => this.onConnect());
        this.bot.on('error', (err) => console.error('Error :', err.message));
        this.bot.on('kick_disconnect', (reason) => this.onKickDisconnect(reason));
        this.bot.on('login', () => this.onLogin());
        this.bot.on('plugin_message', (channel, data) => this.onPluginMessage(channel, data));
        this.bot.on('custom_payload', (packet) => this.onCustomPayload(packet));
        this.bot.on('end', () => this.onDisconnected());
    }

    onConnect() {
        console.log('Connecting to ', this.ip, ':', this.port);
    }

    onKickDisconnect(reason) {
        console.log('Kicked:', reason);
    }

    onLogin() {
        console.log(`Connected at ${this.ip}:${this.port} with ${this.mode.toUpperCase()} MODE.`);
    }

    onPluginMessage(channel, data) {
        if (channel === 'minecraft:brand') {
            this.brand = data.toString('utf8');
            this.gotBrand = true;
        }

        if (channel === 'minecraft:register') {
            this.channels = data.toString('utf8').split('\x00').filter(Boolean);
            this.gotChannels = true;
        }

        this.checkReady();
    }

    onCustomPayload(packet) {
        if (packet.channel === 'minecraft:brand') {
            this.brand = packet.data.toString('utf8');
            this.gotBrand = true;
        }

        if (packet.channel === 'minecraft:register') {
            this.channels = packet.data.toString('utf8').split('\x00').filter(Boolean);
            this.gotChannels = true;
        }

        this.checkReady();
    }

    checkReady() {
        if (this.gotBrand && this.gotChannels && !this.ready) {
            this.onReady();
        }
    }

    onReady() {
        this.ready = true;

        console.log('Server brand:', this.brand || 'Nothing.');
        console.log('Channels:', this.channels.length > 0 ? this.channels.join(', ') : 'Nothing.');

        const result = {
        ip: this.ip,
        port: this.port,
        brand: this.brand || null,
        channels: this.channels
        };
        console.log(JSON.stringify(result, null, 2));
        this.bot.end();

        // Exemple de payload
        /*
        if (this.channels.includes('sr:messagechannel')) {
            this.sendPluginPayload('sr:messagechannel', { skinName: 'Notch' });
        }
        setTimeout(() => {
            this.bot.end();
        }, 2000);
        */
    }

    // Méthode pour envoyer un payload JSON sur un canal spécifique
    /*
    sendPluginPayload(channel, payloadJson) {
        try {
            const buffer = Buffer.from(JSON.stringify(payloadJson), 'utf8');
            this.bot.write('plugin_message', {
                channel: channel,
                data: buffer
            });
            console.log(`[→] Payload envoyé sur ${channel}`);
        } catch (err) {
            console.error(`⚠️ Erreur d'envoi payload sur ${channel}:`, err.message);
        }
    }
    */

    onDisconnected() {
        if (!this.hasRetried && this.mode === 'none') {
            this.hasRetried = true;
            console.log('🔁 Tentative en mode FAKEHOST...');
            new MinecraftBot({
                ip: this.ip,
                port: this.port,
                username: this.username,
                mode: 'fakehost'
            });
        } else {
            console.log('Finish.');
        }
    }
}

// --- ENTRYPOINT ---
const ip = process.argv[2];
const portStr = process.argv[3];
const port = parseInt(portStr);
const mode = process.argv[4] === 'fakehost' ? 'fakehost' : 'none';

const bot = new MinecraftBot({
    ip,
    port,
    username : mode === 'fakehost' ? 'FTool-Scanner' : 'FTool',
    mode
});
