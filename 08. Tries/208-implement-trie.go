package tries

// Leetcode 208

// Create Trie Struct
type Trie struct {
	children  [26]*Trie
	endOfWord bool
	root      *Trie
}

// Initialize Trie
func Constructor() Trie {
	return Trie{
		children:  [26]*Trie{},
		endOfWord: false,
		root:      &Trie{}}
}

// Insert Function
func (this *Trie) Insert(word string) {
	// check if empty
	if len(word) == 0 {
		return
	}

	// initialize at cur
	cur := this.root
	// go through the word
	for i := 0; i < len(word); i++ {
		// normalize index
		index := word[i] - 'a'
		if cur.children[index] == nil {
			// if doesn't exist then initialize
			cur.children[index] = &Trie{}
		}
		// else last char at the current
		cur = cur.children[index]
	}
	// set endOfWord is True
	cur.endOfWord = true
}

// Search function
func (this *Trie) Search(word string) bool {
	// as always initialize
	cur := this.root
	// go through the word
	for i := 0; i < len(word); i++ {
		// normalize index
		index := word[i] - 'a'
		// check if empty then return false
		if cur.children[index] == nil {
			return false
		}
		// else loop till the last char at the cur
		cur = cur.children[index]
	}
	return cur.endOfWord
}

// StartWith function
func (this *Trie) StartsWith(prefix string) bool {
	// Initialize
	cur := this.root
	// check if the len is size of 1
	for i := 0; i < len(prefix); i++ {
		// normalize index
		index := prefix[i] - 'a'
		// check if empty then return false
		if cur.children[index] == nil {
			return false
		}
		// else loop till the last char at the cur
		cur = cur.children[index]
	}
	return true
}
