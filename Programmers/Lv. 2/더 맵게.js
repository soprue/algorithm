class MinHeap {
    constructor() {
        this.heap = [];
    }
    
    push(val) {
        this.heap.push(val);
        let currentIndex = this.heap.length - 1;

        while (
          currentIndex > 0 &&
          this.heap[currentIndex] < this.heap[Math.floor((currentIndex - 1) / 2)]
        ) {
          const temp = this.heap[currentIndex];
          this.heap[currentIndex] = this.heap[Math.floor((currentIndex - 1) / 2)];
          this.heap[Math.floor((currentIndex - 1) / 2)] = temp;
          currentIndex = Math.floor((currentIndex - 1) / 2);
        }
    }
    
    pop() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const minValue = this.heap[0];
        this.heap[0] = this.heap.pop();
        let currentIndex = 0;

        while (currentIndex * 2 + 1 < this.heap.length) {
            let minChildIndex = currentIndex * 2 + 2 < this.heap.length && this.heap[currentIndex * 2 + 2] < this.heap[currentIndex * 2 + 1] ? currentIndex * 2 + 2 : currentIndex * 2 + 1;

            if (this.heap[currentIndex] < this.heap[minChildIndex]) break;

            const temp = this.heap[currentIndex];
            this.heap[currentIndex] = this.heap[minChildIndex];
            this.heap[minChildIndex] = temp;
            currentIndex = minChildIndex;
        }

        return minValue;
    }

    peek() {
        return this.heap[0];
    }

    size() {
        return this.heap.length;
    }
}

function solution(scoville, K) {
    const minHeap = new MinHeap();
    scoville.forEach(scov => minHeap.push(scov));

    let count = 0;

    while (minHeap.peek() < K) {
        if (minHeap.size() < 2) {
            return -1;
        }

        const first = minHeap.pop();
        const second = minHeap.pop();
        const newScoville = first + second * 2;
        minHeap.push(newScoville);
        count++;
    }

    return count;
}
