import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NouvelleCollecteForm from "./NouvelleCollecteForm";

class NouvelleCollecteModal extends Component {
  state = {
    modal: false,
  };

  toggle = () => {
    this.setState((previous) => ({
      modal: !previous.modal,
    }));
  };

  render() {
    const create = this.props.create;

    var title = "Edition de la collecte";
    var button = <Button onClick={this.toggle}>Edit</Button>;
    if (create) {
      title = "Creation de la nouvelle collecte";

      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px" }}
        >
          Liste des Collectes
        </Button>
      );
    }

    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <NouvelleCollecteForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              collecte={this.props.collecte}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NouvelleCollecteModal;
