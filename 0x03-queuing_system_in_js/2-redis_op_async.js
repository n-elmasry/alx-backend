import redis from 'redis';
import { promisify } from 'util';


const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server: ERROR_MESSAGE')
})

/**
 * @param {string} schoolName
 * @param {string0} value
 */


function setNewSchool(schoolName, value) {
    client.set(schoolName, value,redis.print);
}


const getAsync = promisify(client.get).bind(client)
/**
 *  @param {string} schoolName
*/

async function displaySchoolValue(schoolName) {
    try {
        const reply = await getAsync(schoolName)
        console.log(`${reply}`);


    } catch (err) {
            console.log(`Error retrieving key: ${err}`);
    }
}


(async () => {
     await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
