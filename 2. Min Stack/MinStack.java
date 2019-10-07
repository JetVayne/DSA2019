package MinStack;

public class MinStack {
	class Node{
		int data;
		int currMin;
		Node nextNode;
		public Node(int initVal, Node newNode) {
			data = initVal;
			currMin = initVal;
			nextNode = newNode;
		}
	}
	
	Node topNode;
	
	public void push(int newVal) {
		if(topNode == null) {
			topNode = new Node(newVal,null);
		}else {
			int temp = topNode.currMin;
			topNode = new Node(newVal, topNode);
			if(temp < topNode.currMin) {
				topNode.currMin = temp;
			}
		}
	}
	
	public void pop() {
		if(topNode==null) {
			return;
		}	
		
		topNode = topNode.nextNode;	
	}
	
	public Integer top() {
		int result = 0;
		if(topNode==null) {
			return null;
		}
		result = topNode.data;
		return result;
	}
	
	public Integer getMin() {
		int result = 0;
		if(topNode==null) {
			return null;
		}
		result = topNode.currMin;
		return result;
	}

}
