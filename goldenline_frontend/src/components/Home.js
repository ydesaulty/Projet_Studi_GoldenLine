import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import CombinedList from "./CombinedList";
import NouvelleCollecteModal from "./NouvelleCollecteModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    collectes: []
  };

  componentDidMount() {
    this.resetState();
  }

  getCollecte = () => {
    axios.get(API_URL).then(res => this.setState({ collectes: res.data }));
  };

  resetState = () => {
    this.getCollecte();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <CombinedList
              collectes={this.state.collectes}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NouvelleCollecteModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;