import React from "react";
import "./styles.scss";
import {Button, Stack} from '@chakra-ui/react';
import {FaBeer, FaGasPump} from 'react-icons/fa'
import {BiTime, GiPriceTag, GrMoney, MdAvTimer} from 'react-icons/all';
type ContainerProps = {};

const ChartTypeSelector = (props: ContainerProps) => {
  return <>
  <Stack direction="row" spacing={4}>
  <Button rightIcon={<FaGasPump />} colorScheme="teal" variant="solid">
    Avg Gas Price
  </Button>
  <Button leftIcon={<GrMoney />} colorScheme="teal" variant="outline">
    Coin Price
  </Button>
    <Button rightIcon={<GiPriceTag />} colorScheme="teal" variant="outline">
    Avg Tx Price
  </Button>

    <Button rightIcon={<BiTime />} colorScheme="teal" variant="outline">
    Avg Tx Time
  </Button>

    <Button rightIcon={<MdAvTimer />} colorScheme="teal" variant="outline">
    Last Block Time
  </Button>
</Stack>
  </>;
};

export default ChartTypeSelector;
