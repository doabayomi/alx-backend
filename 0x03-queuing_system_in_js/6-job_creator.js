import { createQueue } from 'kue';

const queue = createQueue({ name: 'push_notification_code' });
queue.create('push_notification_code', {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
});

queue.on('job saved', (job) => {
  console.log(`Notification job created: ${job.id}`);
});

queue.on('job complete', () => {
  console.log('Notification job completed');
});

queue.on('job failed', () => {
  console.log('Notification job failed');
});
