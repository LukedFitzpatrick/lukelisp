#include <iostream>
#include <vector>
#include <regex>
#include <string>
#include "tokenise.h"

const std::string VERSION = "0.01";


int main()
{
    std::cout<<"LukeLisp v"<< VERSION << std::endl;
    while(true)
    {
	std::string program;
	std::getline (std::cin, program);

	auto tokens = Tokenise::tokenise(program);
	Tokenise::printVector(tokens);
    }
}
