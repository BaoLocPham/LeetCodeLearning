class MyQueue {
    /*
    * This approach:
    * O(n) for push
    * O(1) for pop
    * */
    Stack<Integer> s1 = new Stack<>();
    Stack<Integer> s2 = new Stack<>();
    int front;
    /** Push element x to the back of queue. */
    public void push(int x) {
        if (s1.empty()){
            front = x;
        }
        while (!s1.isEmpty()){
            s2.push(s1.pop());
        }
        s1.push(x);
        while (!s2.isEmpty()){
            s1.push(s2.pop());
        }
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        int rs = s1.pop();
        if (!s1.isEmpty()){
            front = s1.peek();
        }
        return rs;
    }

    /** Get the front element. */
    public int peek() {
        return front;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return s1.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */