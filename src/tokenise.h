#include <iostream>
#include <vector>
#include <regex>
#include <string>


namespace Tokenise
{


// split a char by a delimiter    
std::vector<std::string> split(const std::string& input, const char delimiter);

// given a program, turn it into a list of tokens
std::vector<std::string> tokenise(std::string program);

// helper function, prints a vector of strings	
void printVector(std::vector<std::string> v);
}
