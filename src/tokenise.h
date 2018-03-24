#include <iostream>
#include <regex>
#include <string>

namespace Tokenise
{
// split a char by a delimiter
std::deque<std::string> split(const std::string &input, const char delimiter);

// given a program, turn it into a list of tokens
std::deque<std::string> tokenise(std::string program);

// helper function, prints a deque of strings
void printDeque(std::deque<std::string> v);
}
