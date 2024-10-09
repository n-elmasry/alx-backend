import { createQueue } from "kue";

const blacklisted = [
    { phoneNumber: '4153518780' },
    { phoneNumber: '4153518781' }
]

const queue = createQueue()

function sendNotification (phoneNumber, message, job, done) {
    job.progress(0, 100)

    for(let i = 0; i < blacklisted.length; i++){
        if (phoneNumber === blacklisted[i].phoneNumber) {
            return done(new Error(`Phone number ${phoneNumber} is blacklisted`))
        }
    }
    job.progress(50,100)

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();


}
queue.process('push_notification_code_2', 2, (job, done) => {
    const {phoneNumber, message} = job.data;
    sendNotification(phoneNumber, message, job, done)
})
