import React, { Component } from "react";
import { Table } from "reactstrap";
import NouvelleCollecteModal from "./NouvelleCollecteModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class CombinedList extends Component {
  render() {
    const combined_collecte = this.props.combined_collecte;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Prix categorie</th>
            <th>Date collecte</th>
            <th>Total Achat</th>
            <th>id_client</th>
            <th>id_article</th>
            <th>Quantite article</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!combined_collecte || combined_collecte.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            combined_collecte.map(collecte => (
              <tr key={collecte.id_collecte}>
                <td>{collecte.cat_achat}</td>
                <td>{collecte.prix_categorie}</td>
                <td>{collecte.date_collecte}</td>
                <td>{collecte.montant_achat}</td>
                <td>{collecte.qte_article}</td>
                <td>{collecte.csp_lbl}</td>
                <td>{collecte.description}</td>
                <td align="center">
                  <NouvelleCollecteModal
                    create={false}
                    collecte={collecte}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={collecte.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default CombinedList;