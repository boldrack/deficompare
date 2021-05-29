import React from "react";
import { render } from "@testing-library/react";
import ChartTypeSelector from './ChartTypeSelector';

test("renders without crashing", () => {
  const { baseElement } = render(<ChartTypeSelector />);
  expect(baseElement).toBeDefined();
});
