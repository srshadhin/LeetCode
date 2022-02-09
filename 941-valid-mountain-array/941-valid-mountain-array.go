func validMountainArray(arr []int) bool {
	if len(arr) < 3 {
		return false
	}

	first := 0
	last := len(arr) - 1
    for (first + 1) < len(arr) - 1 && arr[first] < arr[first + 1] {
        first+=1
	}

    for (last - 1) > 0 && arr[last] < arr[last - 1] {
        last-=1
	}
        return first==last
    
}