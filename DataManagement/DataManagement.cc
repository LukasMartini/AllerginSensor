#include "DataManagement.h"

DataManagement::DataManagement(std::shared_ptr<Input*> i, std::shared_ptr<Output*> o): 
    fields{std::make_unique<DataManagementImpl*>(new DataManagementImpl{i, o})} {}

/*
    Preconditions: Data object is in a valid state.
    Postconditions: None.
    Description: receive_data() is called by the associated Input object to notify it of a change.
*/
void DataManagement::receive_data() {
    std::shared_ptr<Data*> temp = (*((*fields)->in))->get_state();
    if (!(*temp)->is_valid()) throw InvalidInputException{};
    (*fields)->received_data = (*((*fields)->in))->get_state();
}

/*
    Preconditions: Data object is in a valid state.
    Postconditions: None.
    Description: Notifies the associated Output object that there is newly injested data to output.
*/
void DataManagement::pass_data() const {
    if (!(*((*fields)->ingested_data))->is_valid()) throw InvalidInputException{};
    (*((*fields)->out))->receive_data(((*fields)->ingested_data));
}

/*
    Preconditions: Data object is in a valid state
    Postconditions: Formatted Data object is in a valid state
    Description: Formats injested data to a standard type such that it can be outputted consistently.
*/
void DataManagement::ingest_data() {
    if (!(*((*fields)->received_data))->is_valid()) throw InvalidInputException{};
    std::shared_ptr<FormattedData*> temp = parse_data((*fields)->received_data);
    if (!(*temp)->is_valid()) throw InvalidInputException{};
    (*fields)->ingested_data = temp;
}
