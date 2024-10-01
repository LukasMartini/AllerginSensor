#ifndef INPUT_H
#define INPUT_H

#include <memory>

#include "../DataManagement/DataManagement.h"

class Input {
    std::unique_ptr<DataManagement*> associated_data_management_module;
    std::shared_ptr<Data*> raw_input;

    virtual std::shared_ptr<Data*> determine_state() const = 0;
    virtual bool poll_source() = 0;

    public:
        std::shared_ptr<Data*> get_state() const;
        void pass_data() const;
        void update_data(std::shared_ptr<Data*> new_data);
};

#endif
