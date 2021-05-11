import React, { Component } from "react";
import { View, StyleSheet, FlatList } from "react-native";
import {
  Text,
  Button,
  Title,
  ProgressBar,
  List,
  Divider,
} from "react-native-paper";

export default class HomeScreen extends Component {
  state = {
    /** @type {import("./types").StarData[]} */
    data: [],
  };
  componentDidMount() {
    this.fetchData();
  }
  fetchData = async () => {
    const res = await fetch("https://fp-star-galore.vercel.app/");
    const stars = await res.json();
    this.setState({ data: stars.data });
  };
  /** @type {import("react-native").ListRenderItem<import("./types").StarData>} */
  renderItem = ({ item, index }) => (
    <>
      <List.Item
        title={item.name}
        description={`${item.distance.toFixed(2)} light years from Earth`}
        onPress={() => this.navigation.navigate("Details", { item })}
      />
      <Divider />
    </>
  );
  /**
   * @type {import("react-navigation").NavigationScreenProp}
   */
  navigation = this.props.navigation;
  render() {
    return (
      <View style={styles.container}>
        {this.state.data.length === 0 ? (
          <View
            style={{
              justifyContent: "center",
              width: "80%",
              height: "100%",
            }}
          >
            <ProgressBar indeterminate />
          </View>
        ) : (
          <>
            <Title style={styles.center}>Star Galore</Title>
            <FlatList
              style={styles.fullWidth}
              data={this.state.data}
              renderItem={this.renderItem}
              keyExtractor={(_, i) => i.toString()}
            />
          </>
        )}
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    backgroundColor: "lightblue",
  },
  center: {
    textAlign: "center",
  },
  fullWidth: {
    width: "100%",
  },
});
