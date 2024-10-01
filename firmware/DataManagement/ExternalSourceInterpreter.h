#ifndef EXTERNALSOURCEINTERPRETER_H
#define EXTERNALSOURCEINTERPRETER_H

#include "DataManagement.h"
#include "../Input/ExternalSourceInput.h"

class ExternalSourceInterpreter: public DataManagement {
    public:
        ExternalSourceInterpreter(std::shared_ptr<ExternalSourceInput*> i, std::shared_ptr<Output*> o);
};

#endif
