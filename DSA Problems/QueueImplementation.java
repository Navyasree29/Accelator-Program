class Queue {
    int[] arr = new int[10];
    int front = 0, rear = -1, size = 0;

    void enqueue(int x) {
        if (size < arr.length) {
            rear = (rear + 1) % arr.length;
            arr[rear] = x;
            size++;
        }
    }

    void dequeue() {
        if (size > 0) {
            System.out.println("Dequeued: " + arr[front]);
            front = (front + 1) % arr.length;
            size--;
        }
    }

    void display() {
        System.out.print("Queue: ");
        for (int i = 0; i < size; i++) {
            System.out.print(arr[(front + i) % arr.length] + " ");
        }
        System.out.println();
    }
}

public class QueueImplementation {
    public static void main(String[] args) {
        Queue q = new Queue();
        q.enqueue(1);
        q.enqueue(2);
        q.dequeue();
        q.enqueue(3);
        q.display();
    }
}
