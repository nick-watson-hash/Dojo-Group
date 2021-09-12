class Node {
    constructor(value) {
        this.value  = value
        this.next = null
    }
}

class SLL {
    constructor() {
        this.head = null
    }

    contains(value) {
        var success = this.head
        while(success) {
            if(success.value === value) {
                return true
            }
            success = success.next
        }
        return false
    }
}
var mySLL = new SLL()
mySLL.contains(10)
mySLL.contains(158)
console.log(mySLL)