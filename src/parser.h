#include <boost/lexical_cast.hpp>
#include <deque>
#include <iostream>
#include "atoms.h"

namespace Parser
{
  
class Expr
{
public:
  void AddChild(Expr* a) { mChildren.push_back(a); }
  void FillAsAtomFromToken(std::string token);

  std::deque<Expr*> mChildren;
  std::unique_ptr<Atom::Atom> mAtom;
};


// build an AST from a deque of string tokens
Expr* tokensToExpr(std::deque<std::string>* tokens);

// helper function, prints an AST with nice formatting
void printAst(Expr* head, int currentDepth=0);
  
}
