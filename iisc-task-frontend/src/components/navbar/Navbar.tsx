import { Flex, Box, Link, Heading, Spacer } from '@chakra-ui/react'
export default function Navbar() {
    return <Flex  alignItems='center' gap='2' flexWrap="wrap" justifyContent="center">
        <Box p='2'>
            <Heading size='md'>Image Detection</Heading>
        </Box>
        <Spacer />
        <Flex alignItems="center" gap="2" mx="2"> 
            <Link>Home</Link>
            <Link>About</Link>
            <Link>Contact</Link>
        </Flex>
    </Flex>
}