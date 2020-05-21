package main

import (
	"fmt"
	"log"
)

func isPrime(x int) bool {

	/*
		Base cases:
		- return false if x is even
		- return false if x is 1
	*/
	if x%2 == 0 || x == 1 {
		return false
	}

	/*
		Loop through the odd numbers from 3 to x and check if x is divisible by
		any of those odd numbers and if it is return false.
	*/
	for i := 3; i <= x; i += 2 {
		if x%i == 0 && x != i {
			return false
		}
	}

	return true
}

func main() {

	fmt.Print("\nEnter a number: ")
	var x int
	_, err := fmt.Scanf("%d", &x)

	if err != nil {
		log.Fatal(err)
	}

	if isPrime(x) {
		fmt.Println("The number you entered is a prime number!")
	} else {
		fmt.Println("The number you entered is a NOT prime number!")
	}
	fmt.Println()
}
