const mc = require('minecraft-protocol');

if (process.argv.length < 3 || !process.argv[2].includes(':')) {
  console.log('Usage: node bot.js <ip:port>');
  process.exit(1);
}

const [ip, portStr] = process.argv[2].split(':');
const port = parseInt(portStr);
if (isNaN(port) || port < 1 || port > 65535) {
  console.log('Invalide port number. Please provide a valid port (1-65535).');
  process.exit(1);
}
const username = 'FTool';

const fakeHost = `${ip}\x00127.0.0.1\x00e9e21092-7627-4ff0-9f11-b9898d0beb42`;

let serverBrand = '';
let pluginChannels = [];

const bot = mc.createClient({
  host: ip,
  port: port,
  username: username,
  version: false,
  fakeHost: fakeHost
});

bot.on('login', () => {

    console.log('Connected at ' + ip + ':' + port + ' as ' + username + ' with BUNGEEHACK.');
    console.log('Server brand:', serverBrand ? serverBrand : 'Nothing.');
    console.log('Channels:', pluginChannels.length > 0 ? pluginChannels.join(', ') : 'Nothing.');
    bot.end();

});

bot.on('customPayload', (packet) => {
    if (packet.channel === 'minecraft:brand') {
        serverBrand = packet.data.toString('utf8');
    }

    if (packet.channel === 'minecraft:register') {
        const data = packet.data.toString('utf-8');
        pluginChannels = data.split('\x00').filter(x => x.length > 0);
    }
});

bot.on('end', () => {
  console.log('❌ Déconnecté');
});

bot.on('error', (err) => {
  console.error('⚠️ Erreur :', err.message);
});