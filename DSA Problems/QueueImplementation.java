/*Q1.Implement a Queue data structure using an array. 
Support the operations: 
 enqueue(x) – insert an element 
 dequeue() – remove an element 
 display() – print queue elements 
Input Example: 
enqueue 1 
enqueue 2 
dequeue 
enqueue 3 
display 
Output Example: 
Dequeued: 1 
Queue: 2 3 
Hint for Students: 
�
� Maintain two indices: front and rear. 
�
� Wrap around when using a circular array. 
�
� Increment front when dequeuing, increment rear when enqueuing. */
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
