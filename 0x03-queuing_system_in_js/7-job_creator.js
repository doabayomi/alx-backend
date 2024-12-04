import { createQueue } from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const queue = createQueue({ name: 'push_notification_code_2' });
jobs.forEach((job) => {
  queue.create('push_notification_code_2', {
    phoneNumber: job.phoneNumber,
    message: job.message,
  });
});

queue.on('job saved', (job) => {
  console.log(`Notification job created: ${job.id}`);
});

queue.on('job complete', (id) => {
  console.log(`Notification job ${id} completed`);
});

queue.on('job failed', (id, err) => {
  console.log(`Notification job ${id} failed: ${err}`);
});

queue.on('job progress', (job) => {
  console.log(`Notification job ${job.id} ${job.progress} complete`);
});
