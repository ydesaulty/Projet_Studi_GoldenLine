import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NouvelleCollecteForm extends React.Component {
  state = {
    id_collecte: 0,
    prix_categorie: "",
    date_collecte: "",
    montant_achat: "",
    id_client: "",
    id_article: "",
    qte_article: ""
  };

  componentDidMount() {
    if (this.props.collecte) {
      const { id_collecte, prix_categorie, date_collecte, montant_achat, id_client, id_article, qte_article } = this.props.collecte;
      this.setState({ id_collecte, prix_categorie, date_collecte, montant_achat, id_client, id_article, qte_article });
    }
  }

  onChange = e => {
    this.setState({ [e.target.id_collecte]: e.target.value });
  };

  createCollecte = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editCollecte = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.id_collecte, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.collecte ? this.editCollecte : this.createCollecte}>
        <FormGroup>
          <Label for="prix_categorie">Prix categorie:</Label>
          <Input
            type="number"
            name="prix_categorie"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.prix_categorie)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="date_collecte">Date collecte:</Label>
          <Input
            type="date"
            name="date_collecte"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.date_collecte)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="montant_achat">Total Achat:</Label>
          <Input
            type="number"
            name="montant_achat"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.montant_achat)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="id_client">id_client:</Label>
          <Input
            type="number"
            name="id_client"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.id_client)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="id_article">id_article:</Label>
          <Input
            type="number"
            name="id_article"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.id_article)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="qte_article">Quantite article:</Label>
          <Input
            type="number"
            name="qte_article"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.qte_article)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NouvelleCollecteForm;