#include "tokenise.h"
#include "parser.h"
#include <iostream>
#include <regex>
#include <string>
#include <vector>
#include <map>

const std::string VERSION = "0.01";

class FunctionArgs
{
};


class EnvironmentEntry
{
public:
  EnvironmentEntry(bool isFunction) {mIsFunction = isFunction;}
  virtual std::string ToString() = 0;
  bool mIsFunction;
};


class VariableEnvironmentEntry : public EnvironmentEntry
{
public:
  VariableEnvironmentEntry(Atom::Atom* val)
    : EnvironmentEntry(true)
  {
    mValue.reset(val);
  };
  std::string ToString() { return mValue->ToString(); }
  std::unique_ptr<Atom::Atom> mValue;
};


class FunctionEnvironmentEntry : public EnvironmentEntry
{
public:
  FunctionEnvironmentEntry(std::function<Atom::AtomType(FunctionArgs)> func)
    : EnvironmentEntry(true)
  {
    mFunction = func;
  }

  std::string ToString() { return "A function"; }
  
  // If we're a function, this is our value: A function that takes a
  // FunctionArgs and returns an AtomType.
  std::function<Atom::AtomType(FunctionArgs)> mFunction;
};


class Environment
{
public:
  Environment()
  {
    // std environment members
    // TODO read these from a file?
    AddMember("pi", new VariableEnvironmentEntry (new Atom::FloatAtom(3.14)));
    AddMember("ten", new VariableEnvironmentEntry (new Atom::IntAtom(10)));
  }
    
  std::map<std::string, std::unique_ptr<EnvironmentEntry>> mContents;
  void AddMember(std::string name, EnvironmentEntry* value)
  {
    mContents[name].reset(value);
  }

  EnvironmentEntry* GetValue(std::string name)
  {
    return (mContents[name]).get();
  }
};


int main()
{
  std::cout << "LukeLisp v" << VERSION << std::endl;

  // TODO read these as command line arguments
  bool TOKENISE_VERBOSE = false;
  bool PARSE_VERBOSE = true;

  Environment env;
  
  std::cout << "Env pi: " << env.GetValue("pi")->ToString() << std::endl;
  std::cout << "Env 10: " << env.GetValue("ten")->ToString() << std::endl;
  //std::cout << "Env +: " << env.GetValue("+")->ToString() << std::endl;

  
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
