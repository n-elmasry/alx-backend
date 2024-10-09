import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server: ERROR_MESSAGE')
})


client.subscribe('holberton school channel', () => {

})

client.on('message', (Channel, message) => {
    console.log(`Received message from channel ${Channel}: ${message}`)

    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel', () => {
    });
    client.quit();
    }
});
