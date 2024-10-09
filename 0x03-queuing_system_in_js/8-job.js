import { createQueue } from "kue";


function createPushNotificationsJobs (jobs, queue) {


    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array')
    }

    for ( let i = 0; i < jobs.length; i++) {
        const jobData = jobs[i]
        const job = queue.create('push_notification_code_3', jobData)

        job.save((err) => {
            if (err) {
                console.log(`Failed to create job: ${err}`)
                return;
            }
            console.log(`Notification job created: ${job.id}`)
        })

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`)
        })

        job.on('failed', (errorMessage) => {
            console.log(`Notification job ${job.id} failed: ${errorMessage}`)
        })

        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`)
        })


    }

}


export default createPushNotificationsJobs;
