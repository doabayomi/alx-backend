import { createQueue } from 'kue';

const blacklistedPhoneNumbers = ['4153518780', '4153518781'];
const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  if (blacklistedPhoneNumbers.includes(phoneNumber)) {
    job.fail(`Phone number ${phoneNumber} is blacklisted`);
    done(job.failed());
  }

  if (job.progress === 50) {
    console.log(`Sending notification to ${phoneNumber}, `
      + `with message: ${message}`);
  }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done();
});
