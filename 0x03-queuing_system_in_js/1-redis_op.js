import { createClient, print } from 'redis';

const client = createClient();
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err.toString());
});

client.on('ready',
  () => console.log('Redis client connected to the server: '));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  const value = client.get(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
