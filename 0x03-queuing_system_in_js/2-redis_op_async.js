import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err.toString());
});

async function setNewSchool(schoolName, value) {
  const setAsync = promisify(client.set).bind(client);
  await setAsync(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const getValueAsync = promisify(client.get).bind(client);
  const value = await getValueAsync(schoolName);
  console.log(value);
}

async function main() {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('ready', () => {
  console.log('Redis client connected to the server: ');
  main();
});
