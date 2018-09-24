https://www.lintcode.com

1376. Equivalent Strings
1375. Substring With At Least K Distinct Characters
824. Single Number IV
787. The Maze
575. Decode String
10. String Permutation II

https://www.lintcode.com/contest/54

class Solution:
    """
    idea: binary search, 4 use cases to move start or end to mid.

    @param nums: The number array
    @return: Return the single number
    """
    def getSingleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            if nums[start] != nums[start + 1]:
                return nums[start]
            if nums[end] != nums[end - 1]:
                return nums[end]
            mid = start + (end - start)//2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    end = mid
                if nums[mid] == nums[mid + 1]:
                    start = mid
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1
                if nums[mid] == nums[mid + 1]:
                    end = mid - 1

test = Solution()
nums = [3,3,2,2,4,5,5]
r = test.getSingleNumber(nums)
print(r)

nums = [2,1,1,3,3]
r = test.getSingleNumber(nums)
print(r)

class Solution:
    """
idea: Divide and conquer, 拆分成左右子任务.
pitfall: need to return False when not match, also 2 level if.
        if len(s1) <= 1:
            if s1 == s2:
                return True
            else:
                return False

    @param s1: a string
    @param s2: a string
    @return: is s1 and s2 are equivalent
    """
    def isEquivalentStrings(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if len(s1) <= 1:
            if s1 == s2:
                return True
            else:
                return False
        # print("s1", s1, s2)
        mid = len(s1) // 2
        if (
            (self.isEquivalentStrings(s1[:mid], s2[:mid]) 
            and 
            self.isEquivalentStrings(s1[mid:], s2[mid:]))
           or 
           (self.isEquivalentStrings(s1[:mid], s2[mid: ]) 
            and 
            self.isEquivalentStrings(s1[mid:], s2[ :mid]))
          ):
            return True
        return False

s1 = "aaba"; s2 = "abaa"
test = Solution()
r = test.isEquivalentStrings(s1, s2)
print(r)

import collections
class Solution:
    """
idea: (棋盘格路径问题)打破思维定式。理解需求描述的时候，要放空思想，抛弃经验，虚心吸收。
core code: next_stops(); is_valid(), visited_loc_set([tuple( )]),
BFS - 找是否存在一条路径。

    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        start = tuple(start)
        destination = tuple(destination)
        return self.bfs(maze, start, destination, steps)
    def bfs(self, maze, start, end, steps):
        visited = set([start])
        q = collections.deque([start])
        while q:
            curt = q.popleft()
            if curt == end:
                return True
            stops = self.next_stops(maze, curt, steps)
            print(stops)
            for stop in stops:
                if stop not in visited:
                    q.append(stop)
                    visited.add(stop)
        print(visited)
        return False
    def next_stops(self, maze, pos, steps):
        stops = []
        for step in steps:
            next_stop = pos
            while self.is_valid(maze, next_stop):
                stop = next_stop
                next_stop = (stop[0] + step[0], stop[1] + step[1])
            stops.append(stop)
        return stops
    def is_valid(self, maze, pos):
        depth = len(maze)
        width = len(maze[0])
        row = pos[0]
        col = pos[1]
        if 0 <= row < depth and 0 <= col < width and maze[row][col] == 0:
            return True
        return False

test = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3, 2]
# destination = [4,4]
r = test.hasPath(maze, start, destination)
print(r)

class Solution:
    """
    idea: 2 pointers.
    
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        count = 0
        size = len(s)
        char_index = {}
        char_set = set()
        i = 0
        j = 0
        while i < size:
            while j < size:
                char_index[s[j]] = j
                char_set.add(s[j])
                if len(char_set) >= k:
                    count += (size - j)
                    break
                j += 1
            if j == size:
                return count
            while i <= j and i <= char_index[s[i]]:
                if i < char_index[s[i]]:
                    count += (size - j)
                    i += 1
                if i == char_index[s[i]]:
                    char_set.remove(s[i])
                    i += 1
                    j += 1
                    break
        return count

test = Solution()
s = "abcabcabcabc"
k = 3
r = test.kDistinctCharacters(s, k)
print(r)

s = "veunvywzrejbyawhzkwzraafgdjoefevaczcjfdknpjdyqhttizpngweiqefbdtzgizxwfvaakeglpldjelvdbuhwcgkjnyzlxsz"
k = 1
r = test.kDistinctCharacters(s, k)  # 5050
print(r)

s = "oomaefujmmijmosnyxxkjoikwkfrhzpkpvbqjmbhrnvfnimzqkugohmoszhmlmzaxdmvtlwldsocldvkwultuzuhbdfbujttbxmn"
k = 15
r = test.kDistinctCharacters(s, k)  # 3033
print(r)

# s = "ikvazfwnrkgzfhjtelfdztdayvextcesghlzgddxtsphufcjomeqhxylbztnqwbtmmlkdhhrpfefqbhoqecphlpjvaxbwxejseltuawziawkfjkgfifzdcfmtygqqykhoiemgifdbakwnasjfkllsvqhimbemawvxzdgbkfhfyntqcepyubghuguywgjhyuyjxuymfktmbeugatqsffpclvvhaaketeooylbcqxnjzkabmagobmiwaygyppnuktjwjvwlzckkrhoxjsselwfsutrebpnuxgrzoxwwboufhqcyngtgckztnemhitvuhrqgzmzrsvpsygncmfvjtuvlnebzrtokbwlyjrifbrgmukjhzusmubmdpgdwuqndlmxaklolbcdxltdyjwurivujyrugjhbyjpwsokvttizmfekfdlyzriacrorsyewzruurmilcduyioujrgoqhddibpjgjlutrbahqfhlbnkkgreakpsurqksotcsxqvctcybupgwwvurmhwoybwxfbfyqvjfpgqpwcrhkcajvighprclqkorkaiwwiiitvscstzriesooqamibqugwplccevavomkczevzfulxfntnsrjrhqytosriqphvuhbnmxfmhknouognxvmfeabyzksmpzgzlokelsvygpbprjwmvzlsbtedxlbmbvhjqoetmqgqtmwftrglxugeehnrpagcnvaitlprkuusxvweriphpeevbldmexdeeodfwwrqxsqjsuliisczynblspeaeqdcsmhiuohymqxetjdvdlitormxncxeadfvieesgtxodstthbrgtgnpqsbikepvyjpuwuwytvrilirwohshzkljgtfcydytrhiwiazosuesbadfmprtewtdhphdnoekhxezczzrfssqczopxzovlvjlyqmteefhmmbejknxnyxwqgxjsfeuksaecoztzfwwkhyllzsstvycmuqcszsfleymseppypfidprrwzsuxnlxnrdhrmejlpvqbcqlhvqnklubgitsvxewfkzhiypcsrxflyfbvvyrttfuqrjcaafamvpwvuyrfzuatgrwakuixtfltrcxtfwmxabtiexbyfgxgdcgijwxoljxabuospekefkgujvalpembcdrfighrlqmbbicppgfxtckekkymjbrpfmdlhmlbfdhdilgmdrgehtthjczgryilyfgphrrdczuutkfzdvklrvbitvrflcjfjrumbxyzrtgzebttmdcrpewyfkwcsrszteecysfkyfbzanrgogwnrqjqbxfmizdmgatbyuabgwgtkiqtplmhakgaednzzzlmorbtcumjfppewngsmwqkmpuwnritsywfiyhthuepnkdmzsyrfogerimwncfbnlsuulsazzfovsawhrdmtqibqcygwlctjoarbdustxswggzgnyfddfekhicywjpmtdebbruadxsypeojqignmgsauxjutkjuluxqppqkfwilkmynxqhvdgtqcjwjhyivzljiggprjtgnfhmnffkypuwjqvmmfgcwyiczbbkjergxttgluxeqzanxuyleubokwadmxqmvxnciyqdbyywjknufeykvovooaykfmnvprzxvktjevazakuzgrignwgodbvyefkvrauxxcxxdmbuhiapppstwfwryuwxktluiznsbstctbmjbkchzjcoixzlcowrstokksdyoqqrijuimvjspmkopfkebscoyqozcmtfpdofdqhpypytiklrxgjfgpgdsnhapxjdhfdsrxemyjykcxvjbqvuqmlodqwofjojaiymxolopqghcfemfjbvtnkhmdtsphewjbtbsdbanzcknpcrgfxlqnqjhmrahecrwimmmfwplogvfcsckwbnmpgqkerrovnzgqyiuucqklufyttdqtlvnomqwwscsgchvwnccescmyppkdsnitevupihscgfkbrlgdpazsimkfcclfflnybzzvaxsxltuzhftjkbogeygbpybknmxcdiyxsnimjblgsgrejzybkymukfxsmzjvlqewvhksypnjlxqrtujhouchctwmohwejpszvotoveghsmsnanrjfypceirstjxhznczqwhxmhtfbsegbuesxvgsmlwpcaensfwxelqjzrpstcaqonbvagjvkwulebezhsojonmzfahwpswidgukiolqgcloztjxpjedystgihmeacamwrkytzicvsasrnqgylzhebfpbulbczasvbdwlhkhqgxpmfmtvaiujmytlcbsfbqaoznimtsrdsgsfgfujpcthvlleqxfrbmhshqymwymvobnynhinyaftxlalrenpziiosvmtgbglvdtoxpnukiuzlrekvgsvjtmrmohwxduvfsjoujivqzfpgfaggmtklkagvenwpwtkubbmlqhinckesshxlvvobjmamrdgecfgrxotlohuoabaawbqtiwnlcuorqjctssjldixnblknigbrmvvezsgqvuvpshvofqdrdqpfyfulmydviewubroavonzcdvrsptwmxfxnrbmjvhzacwronpzebalmtbzpkaqhoxujpbmdagbnvouhwseoyxwqwscelpobshljvmzimusxxxaowpkicooafhhumhjhwlwutbnizkqwttfzzjbbeelvaljisfxswmihzuibecfnashbldqdhkprppmvfqdgejhlomqzfeouhpmyoybluqjebihxpsycmstmshdgabkvigggrpxjaqggzlxjcgxogokfwujquztiqpmchkkgeypnazakaqftvmzupcwmguimbuqctiltnioonelpjlotcrlkazeisskvzswievjcitimjgvjujnpopnvhbclnevepitppqgbkpymbjcsisjmpawwsutqyszyfdbtgckdxscbisngqvnkzkhqzqnlrximajlfzlgcwuntutjcrsubdzitcwuzncaevdqtgpaxpbjyotmlprpripcilddzkhqvxhuabxmjusupfltsbjkpefnbhwavzjhwjvqxxawkmzhdhwywnqvmqtbynuvvusnsxebnmxkszgttsmetnppvpfpqtsbctezwxveqhizsdqdzwlmykvchgpbiutrrbxstmbqgacpzeetncpyvvjzwtugfswescqytzbhkxhwwgqsiedpabakmldgisqwmfkcfiohblvrlzvniecfmkswajwugsaljfubcpbmbjrdskvpwzsgmardqsvcpaouikfqeedpqrmmrhcruqtquugmcesuccxmrthfqnudmtbplvxdsmyevfodrcjxizaqisgzgycjgdyukixhdijzntpxpsybstpooupmebpmaauzugshfskiqecpccsvyarcvkhlyedebfmnkrhuznzzehgqzbzovrhfhkoouibygpqjkzxjtofnjapehnbkenbqfmvqrppsmaxnyyyxrbqspujewmxrwkufjsntxsrotpvgjryysrmwkieaetnlfkotowytiwpvyyudemhqiuxwlkcujgjkiofuvismjlyoyikycupkwglwkdlcbdojznhufyzrsyeuasexwwnjytxigacogtijduillelefrokbhqjcpzsueynyesdahnjkxrirnlzutovgvdkvuxcavrxeugthcpbhdubwwzhujiltkztldosyzfjdoytfjypeldnqjawbjaxqugvnduooehtgkgdvpkkjodtqtxyzlyrnlcbcmxebqmolrnsaxnbpnzzxqfykhofrlogtemvixdqhujydhsydwpmcpdifwtwtmgocfvmqjtkoxniyihkpkaocotkqsnitlwevwsftenktgwqjfbwoxbhlldtgvslzplhybxvqrvnlrkohsbsdyjpthkykfarsqyjasucktjajyqdowwbmkkxvgdgdfuueicfdglnwxdmzljrfehqhfvubcdutwlxouvmavfabsppjwncyrtxriqnlusmdiddarlfbmknluazhhdktapqjkpbnqkzbwgwabhfkgtcgaexwvxyomsczlyhdjvahhgqhjzdxgdbeantvjfvyjbtyyumnlnnobbduybtnslpklgyutbpfjuldktrzahkcvhsrluyxfysgchkejqtwsrvgdabwpemxojgsxjbvbqjewprojketrnajzjmmidycjgerdcunikeyzfzitujzmvgxriearqkmvvcdqshagzedtyripeectlspdnvuyudpcwtdcjwieosqlcufbtipbjwzuznxttpqyhwtddqbjeufrowedpcbqoqbllnlobyhtztlblcfstovbuuwscgksusvrnfinaukbtxrflcablagwbcfhasvzlgiuofxitpbqrlwqzmqcapqbvubopvdxbwwkaibgjppsobxbmbcdbrnkkmggreftqpduzfqglvavqjymhfbhmpjlpbkyzsnkdafmujiaqipqobvbyzlmaqasyxkhpbspwhgwkcviddmhvwgmmlgyooytdqdwhnfbemtvlyvaangpumuzcupypfgqugdjgsnestfhhbjsdhqhumkjdbgbqmcbbuyjvhaahfkvdaavibftojeovbjiqigedyvyjmmqlmzxbrpsufsjnkmduupllbdazdbjqmltspkxczvxabyweqlxgiudjfidaronbkgfruyihilbhfgvesfncabuzzixwdisogexionqsgalfdmsucglobgxaurkbpmhqpnmaqqedauuxeorxiyanbmnqmmyyyuedivspmgdzdtaricskjuvizyzbpomxblkkmwzqamuraepdvnzngkuuasogdzkganvqchdjqgavssnrskcctbpyealtuiaxpymgtbnusglgxqrlcvoodgjxaatotdadeqxlyxvbiuedkkidswztgomnupknahyuelehvsmxtmjgfmaxslpeevsqnxwilebhdllllfrjapqoqbhftrbajwxqxjwllkwrrsldykizfwddnheqleyfjbhhbakxpsrzzqlmsnwclkninbkuybnxbvwojlrirvnmcadfzuhueuhxcsdhajofejhqvxdshhagjxeeifdeagymxtijcuyotwxzhxwjrinhwrkdlvjcgzjreqqhrditruwxkqkhqywghuhnrxljtimgoykxsrsqzdymlgiivcpssumzjcnmwclpwrhzsxsqlxcvlhvzuqoarcvporpbnlkbddhsmjiizylmckhlvsbgyrahnfeoxcyoieevcgmwwcjcrsjcfnnxejfkdkmpyvevjgajfdecrqkataofokjktnwhxcqzhjozmjcenhtmtfdrnnxqeebfehlsmdkpiuseyrzahudhjenqksjprstguejqypwlbnkgnspzqrcjtotyakwifmhfmccdrwoqsgmnzkaboyvgwbrartsxwuhfidalsgbnxxvntdpbhcyiyjgfdobqhkvvikcrjkelemeaxzcdcawdplvjxgfjdmoxswmosrmxeclyunbtaybxhsfcmruufhjklgjucfraoidealveluproenrgffxhvmlkgxcwwcpvcvxyyiidbexuklnzurrfpvxbaibfgnjgflprbkwxlaalijkwwkgvfjmjrwtbbsfronkemkyjujnkkprwbfcwmspocamtnzfyoskriwoinqaltrvvenrksrvhocpvxnpclelvpinkmgjvsxyixifjszdcvckwqjobgeuoflyomsmukhulcopwvgmvrywlvsqrarrvnygqbpzftccexjqsacegavxnepjprkocwjqqqkevttpjfbcblcsanikbmuxjvvbkdtkhgdkafxwfqtwuosaluodwqvojidlwqdmeyiczizuragvuifnxncdkksijqluhxabsyqbamtaplsmdgzsawlwpnulsuzbybeshrwewmvcpeglxgabejybqvletrlhqwrnfplzchsufxyutdxtoclmoyutqlqdzrplhfebznzyqjsrqpcjyqwmqjfwfcaecsgcyimetdgnqokoafppksbkalqcrgiyjecochkporczvupivctdvdfnlpwbdxdycllqnzmjjbonkmfocfmmugpmmjbzpvxbdiqbaprcaitrxflhuclhzqhxmkyssqwpijpuxykltzxuptxbudfvpuladhtqtpuitquuymiopxzrxghmpzdzyngadyzsnhtiavysqokbdgoulecygskbrcsyaewjieyezjikzonljccahqbkcrztyzstyzybawhzqfuwbglwqnfzwgcllhccnskflmjlfkkorbkufwgvxujknsdzhswbepehxchunlhdljjqxmtawdheszdfczknmshsoorqzdogpfdvcapeeseegbrbfmmgjdwzrdertilpqshkhckxhbavmfnuurtqrkvburbayimpufubuheaijxfckqhfwblshvaqscglyiukgeuwqqsdinypyfyzhxiwhuwicvwpoifimoiexpddgoupiszszryivouiedgracjffsuoclwtfzzndskragapjwvikrgvnqgcozxomawxmcvthsycymrfxwfsghkntungiwkfeczfvcjiifnmgxpvlmjwxldnahkffwybikbqluptmoazvfytnsjgqapqrbmznstwfarrzizgmraxouswleoipgqbwhqrrbjubdxlfdkmzupmtikamnviaxmwugwhwqmclkamtxugnxhghowaaupicxdrrebytaizohxejtnkmfrsjfcamvytxuxtrnakxmtadhfdeehetlzielyyetxwzqcbqrdrfqjkayibiwefcgbvnvnkxtfgpchhnueylbtnabftggskuckjkaitrdhsctqqucghccudolbqfushzcryoxmlvsapqurdgfylfgsfhtnntgmybddabqxychgkpoxnhoowpytbtwbgfxfgitwqulnpbnwtuejwfpolrkjmopzdzyhracxlpppeemzkxwkyzxqvcclumggrpqcmqljlwlvdflmilkwhyyhzluxjrpbibupwzmymrjamibrumkqoskxysalriuehjirdgwpxxizafoqszucwbbthygwmmfkoidkvrgtxhdcfjorusuglvaduyuogvcabugvsdkkpjgttnsmodntjvjgrlteaweycbqgpvzudxlvzufkuhhywykwozgjbhfjbdiphvcbwndcxpdtfhpbkympvmoawrgbeznhwbuojzgbonvpkevhdqdfrgmjbpuwqihunmjtthnxvtianrfvqniudiwgmcrcgiflimlvmxgcpdvqydjjaluycifqbjabnbjmkombxaumnvkwiihcxndshkkapwwjnmwqzhofvplnxudswqmalhbsqrikbqdsjnirorfiwuyyfuelvlvnrknvebpxprymmzkwkgjxeqhiojxojjfcczhbtnfdawmyiatoycfdfdahkyzsojsghwclpzfrwvuitkylklczpxsulkrxbdlvinvmymysodhocyxpqfjdfllvexinyueslmusewjfbtwpzxeuxvdukfwqgxekekrvutrrxrzattudsymwqtqyhuugkxtisaqlalznvfcyjknpsedyxgunjodtjrpuerdgefffhslgyiyoagyjmooukkgmnirprkvrwdgkqtqrlirkuwlzmtpxqzmscuwizbclmqiuzekikijnagiovvgxouqboefuddzfpdcpmrzlnheykpblocbxwavtbnldwavkovnsepurjhsrkcpsjgtxortjcypmgegzqvepzcplxukueahtpqhbhkuawmxuleppmfyosesnfofdzhokavihvtaghodlntiozqjwyoykkbfgbowqkwbthxmondubznyunvyhbptjzbfmdurhdeihznyjmrbrjmoxiymyhvouwqroejgogonotutmkrfjefauzftooxgppceuuwmcgojtaortmqtwfxezwrznithizefzuepbpzslykrzyowkbadqqirflzxnohildswoapikhfesnwhicifyyzpevzbkmbxiduxthszgogkzndeyanfexrevzjnvbysxzswnjhnkwbxzoojznrukwkyxwouzpjmrpgwolnehnclmimogxgsdpjuzjhssuctyaaativkokradqzqimdsawskwjpewazqrwkhhnmtlrkrkkrivnjvoutnzwlqlqxiaxhfjgpbsorgtddcflsxwxcmkrguktwazoqkacboquljmzhkgojsdyestvnboqwavughguiwhhkwwnclrlqkjouhlikusdijewvelzjuilpzxdpzejykzxidqvkwvrbvalucbptavfllbblybdobypycksctyggayyjppmaqdptrgghuhfqktmhsxvqwsqpjnswcdziwssbyzzxusjmqllrzcjabvbwjsxqdgtokmmsexchbwrymqzjwdehmyrlsjtjpirejcxoequgxqepuiptbtaheyzkhbrfbtpuvpyuyuuptirugjpykzzlzrhcoftwrxqmxkdkyeomeoiafpuszsxlzwwhrerfdqhyrkeprymmnjfjdvhhtmzfthsvmunydnrscpumcsrlcgrqbdjgzlvidhommakpwbupkiqqgkjuwazaawfazditsxgdpqlsbfqhcmlvitatucjpqusskaxjisvtlxacgkeiuvucxmducrtntkvnudkcloincsldpscinnqdjlxtymwimtbzxmuzfbpfrhuxjjvsdwsgpehpkazspgppxfyejmcwxfoykzouvqpmhlkaapbuqbxiapbnhlyeqfzlptevbnuetntxpamhsfkogijdrsfzpjwduyjmcsslwrenaashffwsexzcwrtyjadaxsugtqpfpudxfhdbrgowcjfyunqzckwgrubzcdysucffimxrbwxxiohiukypepvoyldtnzhffqugwmasvgghrafulevajnkrpcomktvjekkkbvelniosebkbokogljuzlyfhzoshjdthdahaawwtqqetnbtammjrkojhowwcfelwbtszillbeqzthjqniahnklbjpwfyfhslvkdiphcnemzlolkqgbjilpjsqcywqvortgxqyzhcczysdzsrcngusebqrrlsxrdfbtyxiosufbmphfgmxzigefsxscvmofbxnirifzlavniqfncnjmljhojgcmxefgnpmuuvtofoebmfavlpmduhqcyhzlfysjttmedmjiogtgdevpaigjiggtlooafvyirnfftgkupuqtejedmxggntywrnshfpyntikoypraseguvsamyvaeuteluprsnxbdzefixtpafwrdpmyqrbtyimxtfdnmiucewmmuewvyggmfyialbygpahhiidykfggorjkhlmwhhixqstcxpmcisqurlkfnpbwqjauscjjhrxiisvxlsewwtzvdhjayizznvghgmcgbwrccxdrbwhwpblvfhwvrivohytxoyqzidzakgkxunamyiefluanrddjubbcguhwdqphdptuubpktvwammwxlsuohoezyzdoyonzvcvuwqtalovfmohdeghhasilwawhdbbpzuaqgbwlqcllnopwoyfmueyiqlmrlkuuufpcbydzkaqqqxdjsolqywrcgyvfnxsxxggkiizsaqparqaymvbbboviinzxhfjyldynvuwtdrgswinhgfymomtijpdnzeoorurkvpxfcicwsobumtyrrtrdzjgwywbiccpphnyzrpcnfehttiqdmlumiimlesunvqnwqoyoxxnernuekdsnmoltkoqpanqevwibqjvawcmupwzrbafhgdfwjebayarhevmhsdfmofdxargyypflucivbpsuskfowkgrwtgurjxnzqzw"
# k = 22
# r = test.kDistinctCharacters(s, k)
# print(r)


class Solution:
    """
idea: stack, recursion(divide and conquer), string.find(), int("str")
char index: left, right, pre_left, pre_right

    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        return self.dc(s)
    def dc(self, s):
        if "[" not in s:
            return s
        stack = []
        right = 0
        left = 0
        new_str = ""
        pre_right = 0
        while left != -1:
            left = s.find("[", right)
            stack.append(left)
            while stack:
                right = s.find("]", (left + 1))
                left = s.find("[", left + 1)
                if left == -1 or right < left:
                    pre_left = stack.pop()
                    left = right
                elif left < right:
                    stack.append(left)
            next_exp = s[pre_left + 1: right]
            print(next_exp)
            i = 0
            int_str = ""
            while pre_left - 1 - i >= 0 and "0" <= s[pre_left - 1 - i] <= "9":
                int_str = s[pre_left - 1 - i] + int_str
                i += 1
            new_str = new_str + s[pre_right:pre_left - i] + int(int_str) * self.dc(next_exp)
            pre_right = right + 1
            left = s.find("[", right)
        new_str = new_str + s[pre_right:]
        return new_str


test = Solution()

s = "abc2[x2[y]d2[zz]]c111[d]"
r = test.expressionExpand(s)
print(r)

# s = "abc2[a2[b]]x2[c]"
# r = test.expressionExpand(s)
# print(r)

s = "3[2[ad]3[pf]]xyz"
r = test.expressionExpand(s)
print(r)

