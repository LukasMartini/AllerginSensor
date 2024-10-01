#ifndef DATAMANAGEMENT_H
#define DATAMANAGEMENT_H

#include <memory>

#include "DataManagementImpl.h"
#include "../Input/Input.h"
#include "../Output/Output.h"
#include "../Exceptions/InvalidInputException.h"

class Data;

class DataManagement {
    std::unique_ptr<DataManagementImpl*> fields;
    virtual std::shared_ptr<FormattedData*> parse_data(std::shared_ptr<Data*> data) = 0;

    public:
        DataManagement(std::shared_ptr<Input*> i, std::shared_ptr<Output*> o);

        void receive_data();
        void pass_data() const;
        void ingest_data();
};

#endif
