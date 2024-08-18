#ifndef DATAMANAGEMENT_H
#define DATAMANAGEMENT_H

#include <memory>

#include "DataManagementImpl.h"

class Data;
class Input;
class Output;

class DataManagement {
    std::unique_ptr<DataManagementImpl*> fields;
    virtual void parse_data(std::shared_ptr<Data*> data) = 0;

    public:
        DataManagement(std::shared_ptr<Input*> i, std::shared_ptr<Output*> o);

        void receive_data();
        void pass_data();
        void injest_data();
};

#endif
