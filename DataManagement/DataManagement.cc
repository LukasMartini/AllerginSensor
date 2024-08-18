#include "DataManagement.h"

DataManagement::DataManagement(std::shared_ptr<Input*> i, std::shared_ptr<Output*> o): 
    fields{std::make_unique<DataManagementImpl*>(new DataManagementImpl{i, o})} {}

/*
    Preconditions: None.
    Postconditions: Data object is in a valid state.
    Description: receive_data() is called by the associated Input object to notify it of a change.
*/
void DataManagement::receive_data() {
    
}

/*
    Preconditions: Data object is in a valid state.
    Postconditions: Data object is successfully received by Output object
    Description: Notifies the associated Output object that there is newly injested data to output.
*/
void DataManagement::pass_data() {

}

/*
    Preconditions: Data object is in a valid state
    Postconditions: Formatted Data object is in a valid state
    Description: Formats injested data to a standard type such that it can be outputted consistently.
*/
void DataManagement::injest_data() {

}
