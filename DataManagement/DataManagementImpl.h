#ifndef DATAMANAGEMENTIMPL_H
#define DATAMANAGEMENTIMPL_H

#include <memory>

#include "../Data/FormattedData.h"

class DataManagement;
class Input;
class Output;

class DataManagementImpl {
    std::shared_ptr<Input*> in;
    std::shared_ptr<Output*> out;
    std::shared_ptr<Data*> received_data;
    std::shared_ptr<FormattedData*> injested_data;

    public:
        DataManagementImpl(std::shared_ptr<Input*> i, std::shared_ptr<Output*> o);


    friend class DataManagement;
};

#endif
