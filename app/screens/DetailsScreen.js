import React from "react";
import { Text, View, StyleSheet } from "react-native";
import { Card, Title, Paragraph, Button } from "react-native-paper";

export default class DetailsScreen extends React.Component {
  constructor(props) {
    super(props);
    /**
     * @type {import("react-navigation").NavigationScreenProp}
     */
    const navigation = this.props.navigation;
    /**
     * @type {import("./types").StarData}
     */
    this.item = navigation.getParam("item");
    this.state = { url: "" };
  }
  componentDidMount() {
    this.getImage();
  }
  getImage = async () => {
    const res = await fetch(
      `https://images-api.nasa.gov/search?q=${this.item.name}`
    );
    const json = await res.json();
    this.setState({ url: json.collection.items[0]?.links[0]?.href });
  };
  render() {
    return (
      <View style={styles.container}>
        <Title style={{ textAlign: "center" }}>Details</Title>
        <Card style={{ width: "90%", margin: "auto" }}>
          <Card.Title title={this.item.name} />
          <Card.Content>
            <Paragraph>
              Distance from Earth: {this.item.distance} light years
            </Paragraph>
            <Paragraph>Mass: {this.item.mass} Solar Mass</Paragraph>
            <Paragraph>Radius: {this.item.radius} Solar Radius</Paragraph>
            <Paragraph>
              Acceleration caused by Gravity: {this.item.gravity} m/s²
            </Paragraph>
          </Card.Content>
          <Card.Cover source={{ uri: this.state.url }} height={200} />
          <Text style={{ fontSize: 10 }}>
            {this.state.url
              ? "This Image is brought to you by NASA (C) Image and Video Library"
              : null}
          </Text>
        </Card>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    // flex: 1,
    // alignItems: "center",
    // justifyContent: "center",
  },
});
