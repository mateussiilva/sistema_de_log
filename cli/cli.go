package main

import (
	"fmt"

	"os"
)

// func read_args(args []string) []string {
// 	if len(args) > 1{
// 		return args
// 	}
// 	os.Exit(1)
// 	return []string{}
// }


func main() {
	args := os.Args;
	if len(args) < 2{
		fmt.Println("<PATH FILES HTMLS>")
		os.Exit(1)
	}
	const path_htmls = sli

}
