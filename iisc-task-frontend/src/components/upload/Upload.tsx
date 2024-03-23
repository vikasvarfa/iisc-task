import React from 'react'
import { Box, Button, Container, Flex, Heading, Image, Spinner } from '@chakra-ui/react'
import { useToast } from '@chakra-ui/react'

export default function Upload() {
    const [file, setFile] = React.useState<File>();
    const [processedImagePath, setProcessedImagePath] = React.useState<string>()
    const [originalImagePath, setOriginalImagePath] = React.useState<string>()
    const [loading, setLoading] = React.useState<boolean>(false);

    const toast = useToast();
    const handleSubmit = async () => {
        if (file) {
            setLoading(true);
            try {
                const formData = new FormData();
                formData.append('image', file);
                const response = await fetch('http://localhost:5000/uploads', {
                    method: 'POST',
                    body: formData,
                })
                const data = await response.json();

                setOriginalImagePath(URL.createObjectURL(file))
                setProcessedImagePath(`http://localhost:5000/processed/${data.image}`);
                setLoading(false);
            }
            catch (e) {
                console.error("SOMETHING WENT WRONG!!", e);
                setLoading(false);
            }
        }
    }

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setFile(event.target.files[0]);
        }
    };
    return (
        <>
            <Container my="2rem">
                <Box display="flex" alignItems="center" gap="2rem" flexWrap="wrap" justifyContent="center">
                    <input type="file"
                        accept='.jpg, .png|image/*' onChange={handleInputChange} />
                    <Button variant="solid" colorScheme='blue' onClick={handleSubmit} isLoading={loading}>
                        Submit
                    </Button>
                </Box>
            </Container>

            <Flex alignItems="center" justifyContent="space-evenly" gap="2rem" mx="2rem" flexWrap="wrap">
                {originalImagePath && <Flex flexDirection="column" style={{ width: "min(100%, 20rem)" }}>
                    <Heading size='md'>Original</Heading>
                    <Image src={originalImagePath} alt="Original Image" height="100%" width="100%" /> </Flex>}
                {
                    loading ? <Spinner /> :
                        processedImagePath &&
                        <Flex flexDirection="column" style={{ width: "min(100%, 20rem)" }}>
                            <Heading size='md'>Processed</Heading>
                            <Image src={processedImagePath} alt="Processed Image" height="100%" width="100%" />
                        </Flex>
                }
            </Flex>
        </>
    )
}