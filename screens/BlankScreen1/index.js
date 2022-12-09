
import React from "react";
import { View, StyleSheet } from "react-native";

const BlankScreen1 = () => {
  return <View style={_styles.BlankScreen1}>
      </View>;
};

export default BlankScreen1;

const _styles = StyleSheet.create({
  BlankScreen1: {
    backgroundColor: "#f0f0f1",
    padding: 10,
    position: "relative",
    height: "100%"
  }
});
