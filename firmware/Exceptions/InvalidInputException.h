#ifndef INVALIDINPUTEXCEPTION_H
#define INVALIDINPUTEXCEPTION_H

#include <exception>

class InvalidInputException: public std::exception {
    public:
        const char* what() const noexcept override{
            return "Input data is in an invalid state.";
        }
};

#endif
