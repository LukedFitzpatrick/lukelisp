#include "tokenise.h"
#include "parser.h"
#include <iostream>
#include <regex>
#include <string>
#include <vector>

const std::string VERSION = "0.01";


int main()
{
  std::cout << "LukeLisp v" << VERSION << std::endl;

  // TODO read these as command line arguments
  bool TOKENISE_VERBOSE = false;
  bool PARSE_VERBOSE = true;

  
  while (true)
  {
    std::string program;
    std::getline(std::cin, program);

    // Tokenise
    std::cout << "Tokenise..." << std::endl;
    auto tokens = Tokenise::tokenise(program);
    if(TOKENISE_VERBOSE)
    {
      Tokenise::printDeque(tokens);
    }
    
    // Parse
    std::cout << "Convert to AST..." << std::endl;
    Parser::Expr* ast = Parser::tokensToExpr(&tokens);
    if(tokens.size() != 0)
    {
      throw std::runtime_error("Parser found some junk after expression");
    }
    
    if(PARSE_VERBOSE)
    {
      Parser::printAst(ast);
    }

    delete ast;
  }
}
