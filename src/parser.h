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

  void FillAsAtomFromToken(std::string token)
  {
    // try interpret this token as an int
    try
    {
      int valueAsInt = boost::lexical_cast<int>(token);
      mAtom.reset(new Atom::IntAtom(valueAsInt));
      //std::cout<<"Read "<<token<< " as an int."<<std::endl;
      return;
    }
    catch(boost::bad_lexical_cast const&) {}

    // try interpret this token as a float
    try
    {
      float valueAsFloat = boost::lexical_cast<float>(token);
      mAtom.reset(new Atom::FloatAtom(valueAsFloat));
      //std::cout<<"Read "<<token<< " as a float."<<std::endl;
      return;
    }
    catch(boost::bad_lexical_cast const&) {}

    // otherwise it must be a symbol (e.g. function name, variable name)
    mAtom.reset(new Atom::SymbolAtom(token));
    //std::cout<<"Read "<<token<< " as a symbol."<<std::endl;
  }

  std::deque<Expr*> mChildren;
  std::unique_ptr<Atom::Atom> mAtom;
};





Expr* tokensToExpr(std::deque<std::string>* tokens)
{
  // delete managed by the caller
  Expr* head = new Expr;
  if (tokens->size() == 0)
  {
    throw std::runtime_error("tokensToAst: Unexpectedly got an empty expression");
  }

  // consume the first token
  std::string token = tokens->front();
  tokens->pop_front();

  // start of an expression which contains sub expressions
  if (token == "(")
  {
    //std::cout<<"Started parsing an expression"<<std::endl;
    
    // keep reading until we get to the end of this () block
    while(tokens->front() != ")")
    {
      //std::cout<<"Adding a child expression"<<std::endl;
      head->AddChild(tokensToExpr(tokens));
    }

    //std::cout<<"Finished parsing an expression"<<std::endl;

    // remove the ")"
    tokens->pop_front();
  }

  // unexpected ) at start of expression
  else if (token == ")")
  {
    throw std::runtime_error("tokensToAst: Found ) at the start of expression");
  }

  // must be an atom i.e. an Int, Float, Var name etc.
  else
  {
    head->FillAsAtomFromToken(token);
  }

  return head;
}


void printAst(Expr* head, int currentDepth=0)
{
  // indentation
  for(int i = 0; i<currentDepth; i++)
  {
    std::cout<<"  ";
  }

  // this is an atom
  if(head->mAtom)
  {
    std::cout<<(head->mAtom)->ToString()<<std::endl;
  }
  // this is an expression containing other expressions
  else
  {
    std::cout<<"Expression {"<<std::endl;
    for(auto child : head->mChildren)
    {
      printAst(child, currentDepth+1);
    }

    // indent again (ugly!)
    for(int i = 0; i<currentDepth; i++)
    {
      std::cout<<"  ";
    }
    std::cout<<"}"<<std::endl;
  }
}
  
}
