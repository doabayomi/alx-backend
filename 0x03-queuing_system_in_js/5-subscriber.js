import { createClient } from 'redis';

const client = createClient();
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err.toString());
});

client.on('ready', () => {
  console.log('Redis client connected to the server: ');
  client.subscribe('holberton school channel');
});

client.on('message', (_client, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.quit();
  }
});
