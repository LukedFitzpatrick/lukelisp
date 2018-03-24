#include <string>

namespace Atom
{
  
enum class AtomType { Int, Float, Symbol };

class Atom
{
public:
  Atom(AtomType type) { mType = type; }
  AtomType mType;
  virtual std::string ToString() = 0;
};

class IntAtom : public Atom
{
public:
  IntAtom(int val) :
    Atom(AtomType::Int)
    {
      mValue = val;
    }

  int mValue;
  std::string ToString() { return "IntAtom: " + std::to_string(mValue); }
};

class FloatAtom : public Atom
{
public:
  FloatAtom(float val) :
    Atom(AtomType::Float)
    {
      mValue = val;
    }

  float mValue;
  std::string ToString() { return "FloatAtom: " + std::to_string(mValue); }
};

class SymbolAtom : public Atom
{
public:
  SymbolAtom(std::string val) :
    Atom(AtomType::Symbol)
    {
      mValue = val;
    }
  std::string mValue;
  std::string ToString() { return "SymbolAtom: " + mValue; }
};

}
