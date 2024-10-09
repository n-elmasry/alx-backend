import redis from 'redis';

const client = redis.createClient();

client.on_connect('connect', () => {
    console.log('Redis client connected to the server');
});

client.on_connect('error', (err) => {
    console.log('Redis client not connected to the server: ERROR_MESSAGE')
})
