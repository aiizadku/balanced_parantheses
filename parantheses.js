function balance(str) {

  let rightStack = []
  let leftStack = []


  for(let i = 0; i < str.length; i++) {
    if (str[i] == "(") {
      leftStack.push(i)
    }else if (str[i] == ")") {
      if (leftStack.length > 0) {
        leftStack.pop()
      }else {
        rightStack.push(i)
        // console.log(rightStack)
      }
    }
  }
  

  let combinedStack = rightStack.concat(leftStack)
  let finalStr = ""
  // console.log(combinedStack)

  for(let i = 0; i < str.length; i++) {
    if (!combinedStack.includes(i)) {
      finalStr += str[i]
    }
  }


  return finalStr
}

 console.log(balance("()")) // should return "()"
 console.log(balance("a(b)c)")) // should return "a(b)c"
 console.log(balance("(a)(bdd)c)")) // should return "(a)(bdd)c"
 console.log(balance("a(dbvb)c)")) // should return "a(dbvb)c"
 console.log(balance("a(b)(c)())")) // should return "a(b)(c)()"
 console.log(balance(")(")) // should return ""
 console.log(balance("(((((")) // should return ""
 console.log(balance(")(())(")) // should return "(())"
 console.log(balance("(()()(")) // should return "()()"
 console.log(balance(")())(()()(")) // should return "()()()" 
