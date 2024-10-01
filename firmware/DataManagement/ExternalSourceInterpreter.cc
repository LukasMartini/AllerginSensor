#include "ExternalSourceInterpreter.h"

ExternalSourceInterpreter::ExternalSourceInterpreter(std::shared_ptr<ExternalSourceInput*> i, std::shared_ptr<Output*> o):
    DataManagement{std::make_shared<Input*>(*(i.get())), o} {}
