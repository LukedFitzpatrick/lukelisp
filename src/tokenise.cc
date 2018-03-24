#include "tokenise.h"

namespace Tokenise
{

// split a char by a delimiter
std::deque<std::string> split(const std::string &input, const char delimiter)
{

  std::deque<std::string> words;
  std::stringstream ss(input);
  std::string word;

  while (std::getline(ss, word, delimiter))
  {
    if (!word.empty())
    {
      words.push_back(word);
    }
  }

  return words;
}

// given a program, turn it into a list of tokens
std::deque<std::string> tokenise(std::string program)
{
  // "(" -> " ( " and ")" -> " ) "
  std::regex parenRe("\\(|\\)");
  program = std::regex_replace(program, parenRe, " $& ");
  return split(program, ' ');
}

void printDeque(std::deque<std::string> v)
{
  std::cout << "deque ";
  for (auto s : v)
  {
    std::cout << s << ", ";
  }
  std::cout << "END" << std::endl;
}
}
